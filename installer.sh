#!/bin/bash

function build(){
    base_dir=$(pwd)
    build_path="/tmp/build"
    dist_path="${build_path}/dist"
    work_path="${build_path}"
    spec_path="${build_path}"
    name="hor"

    mkdir -p ${dist_path}

    pyinstaller --contents-directory "." \
        --distpath ${dist_path} \
        --add-data "${base_dir}/conf:conf" \
        --add-data "${base_dir}/hor.cron:." \
        --workpath ${work_path} \
        --specpath ${spec_path} \
        --name ${name} main.py
}

function pack(){
    appname=hor
    package=hor
    section=Misc
    priority=optional
    architecture=amd64
    maintainer="Eli Florêncio Pereira"
    depends="clamav,mutt"
    description="Frontend for clamav and clamscan"
    version=$(cat version)
    cmd_preinst="#!/bin/bash
    ! test -f /etc/${appname}/${appname}.conf || cp -av /etc/${appname}/${appname}.conf /tmp
    "
    cmd_postinst="#!/bin/bash
    test -h /etc/${appname} || ln -s /usr/share/${appname}/conf /etc/${appname}
    test -h /usr/bin/${appname} || ln -s /usr/share/${appname}/${appname} /usr/bin/${appname}
    test ! -f /tmp/${appname}.conf || cp -av /tmp/${appname}.conf /etc/${appname}/${appname}.conf
    cp /usr/share/${appname}/${appname}.cron /etc/cron.d/${appname}
    chmod 0644 /etc/cron.d/${appname}
    "
    cmd_postrm="#!/bin/bash
    ! test -h /etc/hor || unlink /etc/hor
    ! test -h /usr/bin/hor || unlink /usr/bin/hor
    "

    # Apaga builds antigos
    test ! -d /tmp/${package}/DEBIAN || rm -rf /tmp/${package}

    mkdir /tmp/${package}
    mkdir /tmp/${package}/DEBIAN

    {
        echo Section:"${section}";
        echo Package:"${package}";
        echo Priority:"${priority}";
        echo Version:"${version}";
        echo Architecture:"${architecture}";
        echo Maintainer:"${maintainer}";
        echo Depends:"${depends}";
        echo Description:"${description}";
    } > /tmp/${package}/DEBIAN/control

    echo "${cmd_preinst}" >> /tmp/${package}/DEBIAN/preinst
    echo "${cmd_postinst}" >> /tmp/${package}/DEBIAN/postinst
    echo "${cmd_postrm}" >> /tmp/${package}/DEBIAN/postrm

    chmod +x /tmp/${package}/DEBIAN/*
    mkdir -p /tmp/${package}/usr/share

    build

    cp -a /tmp/build/dist/${package} /tmp/${package}/usr/share

    dpkg-deb -Zxz -b /tmp/$package .
    test -d /tmp/${package}/DEBIAN && rm -rf /tmp/$package*
}

function clear(){
    build_path=/tmp/build
    package_name="hor"
    package_build_path=/tmp/${package_name}

    test -d ${build_path} && rm -rf ${build_path}
    test -d ${package_build_path} && rm -rf ${package_build_path}
}

case "$1" in 
    build)
        build
    ;;
    pack)
        pack
    ;;
    clear)
        clear
    ;;
esac

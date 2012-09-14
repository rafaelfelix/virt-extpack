%global debug_package %{nil}

Summary: Ensures the extention pack is present in your virtual machine
Name: virt-extpack
Version: 1
Release: 1
Packager: Rafael Felix Correa <rafael.felix@rf4solucoes.com.br>
License: MIT
Group: System Administration Tools
URL: http://www.rf4solucoes.com.br/virt-extpack
Requires: bash virt-what

BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

Source: virt-extpack-%{version}-%{release}.tar.gz

%description
virt-extpack is a shell script to ensure the installation of the 
extension pack according to the Hypervisor

It depends heavily on the virt-what package (http://people.redhat.com/~rjones/virt-what/).

%prep
%setup -c -n %{name}-%{version}

%install
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d
mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}/var/lib/virt-extpack

cp -a $RPM_BUILD_DIR/%{name}-%{version}/virt-extpack ${RPM_BUILD_ROOT}/etc/init.d/virt-extpack
cp -a $RPM_BUILD_DIR/%{name}-%{version}/virt-extpack-logrotate ${RPM_BUILD_ROOT}/etc/logrotate.d/virt-extpack
cp -a $RPM_BUILD_DIR/%{name}-%{version}/functions ${RPM_BUILD_ROOT}/var/lib/virt-extpack/functions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/init.d/virt-extpack
/etc/logrotate.d/virt-extpack
/var/lib/virt-extpack/functions
# TODO: DOC
#%doc DEVELOPERS.TXT
#%doc INSTALL
#%doc LICENSE
#%doc NEWS
#%doc PACKAGING.TXT
#%doc README
#%doc doc/

%post
chkconfig --add virt-extpack

%changelog
* Sat Aug 03 2012 Rafael Felix Correa <rafael.felix@rf4solucoes.com.br>
- first build of postinstall package

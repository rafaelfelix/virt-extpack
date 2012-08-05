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
#BuildRequires: 

Source: virt-extpack-%{version}.tar.gz

%description
virt-extpack is a shell script to ensure the installation of the 
extension pack according to the Hypervisor

It depends heavily on the virt-what package (http://people.redhat.com/~rjones/virt-what/).

%setup -c -n %{name}-%{version}

%build
$RPM_BUILD_DIR/%{name}-%{version}/bin/passenger-install-apache2-module -a --apxs2-path=/usr/sbin/apxs

%install
mkdir -p ${RPM_BUILD_ROOT}%{passenger_root}/ext
cp -a $RPM_BUILD_DIR/%{name}-%{version}/agents ${RPM_BUILD_ROOT}%{passenger_root}
cp -a $RPM_BUILD_DIR/%{name}-%{version}/ext/apache2 ${RPM_BUILD_ROOT}%{passenger_root}/ext
cp -a $RPM_BUILD_DIR/%{name}-%{version}/ext/ruby ${RPM_BUILD_ROOT}%{passenger_root}/ext

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%exclude %{passenger_ext_apache2}/*.h
%exclude %{passenger_ext_apache2}/*.c
%exclude %{passenger_ext_apache2}/*.cpp
%exclude %{passenger_ext_apache2}/*.hpp
%exclude %{passenger_ext_apache2}/module_libboost_oxt/*.cpp
%exclude %{passenger_ext_apache2}/module_libpassenger_common/*.cpp
%{passenger_ext_apache2}/
%{passenger_root}/agents
%{passenger_root}/ext/ruby
%doc DEVELOPERS.TXT
%doc INSTALL
%doc LICENSE
%doc NEWS
%doc PACKAGING.TXT
%doc README
%doc doc/

%post
rm -f %{apache_module_path}/mod_passenger.so
ln -s %{passenger_ext_apache2}/mod_passenger.so %{apache_module_path}/mod_passenger.so

cat > /etc/httpd/conf.d/passenger.conf << EOF
## load
LoadModule    passenger_module     modules/mod_passenger.so

## setup
PassengerRoot %{passenger_root}
PassengerRuby /opt/ruby/bin/ruby
EOF

## APACHE RESTART
/etc/init.d/httpd restart

%postun
rm -f %{apache_module_path}/mod_passenger.so
rm -f /etc/httpd/conf.d/passenger.conf

## APACHE RESTART
/etc/init.d/httpd restart

%changelog
* Sat Aug 03 2012 Rafael Felix Correa <rafael.felix@rf4solucoes.com.br>
- first build of postinstall package

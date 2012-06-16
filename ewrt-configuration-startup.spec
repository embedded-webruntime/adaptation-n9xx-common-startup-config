Name:       ewrt-configuration-startup 
Summary:    Startup services for embedded webruntime
Version:    3
Release:    1
Group:      Applications/Internet
License:    MPLv2.0
URL:        http://www.e-wrt.com
Source0:    embedded-webruntime.sh
Source1:    embedded-webruntime.desktop

%description
Installs all needed for autostart

%prep

%build

#make

%install
rm -rf %{buildroot}
install -d $RPM_BUILD_ROOT/usr/lib/ewrt/
install -d $RPM_BUILD_ROOT/usr/share/xsessions/
install -D -m 755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/ewrt/
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/xsessions/

ln -sf embedded-webruntime.desktop $RPM_BUILD_ROOT/usr/share/xsessions/default.desktop

%files

%defattr(-,root,root,-)
/usr/lib/ewrt/embedded-webruntime.sh 
/usr/share/xsessions/
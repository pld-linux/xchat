%define name xchat
%define version 0.9.4
%define release 2
%define prefix /usr

Summary: Gtk+ IRC client

Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Copyright: Freely distributable

Url: http://xchat.linuxpower.org

Source: http://xchat.linuxpower.org/files/xchat-%{version}.tar.gz
Source1: xchat.desktop
Source2: xchat.png
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%changelog

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.4

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.3

* Mon Mar 8 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.2

%description
X-Chat is yet another IRC client for the X Window
System, using the Gtk+ toolkit. It is pretty easy
to use compared to the other Gtk+ IRC clients and
the interface is quite nicely designed.

%prep

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=%{prefix} \
	--enable-gnome \
	--disable-perl
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Internet
install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Internet/

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps
install -c -m 664 %{SOURCE2} $RPM_BUILD_ROOT%{prefix}/share/pixmaps/

%files
%defattr(-,root,root)
%doc README ChangeLog
%attr(755,root,root) %{prefix}/bin/xchat
%{prefix}/share/gnome/apps/Internet/xchat.desktop
%{prefix}/share/pixmaps/xchat.png

%clean
rm -r $RPM_BUILD_ROOT

Summary:	Gtk+ IRC client
Summary(pl):	Oparty na Gtk+ klient IRC
Name:		xchat
Version:	0.9.6
Release:	4
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	Freely distributable
URL:		http://xchat.linuxpower.org
Source0:	http://xchat.linuxpower.org/files/%{name}-%{version}.tar.gz
Source1:	xchat.desktop
Source2:	xchat.png
BuildPrereq:	XFree86-devel
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	imlib-devel
Buildroot:	/var/tmp/%{name}-%{version}-root

%define _prefix		/usr/X11R6

%description
X-Chat is yet another IRC client for the X Window
System, using the Gtk+ toolkit. It is pretty easy
to use compared to the other Gtk+ IRC clients and
the interface is quite nicely designed.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--disable-gnome \
	--disable-perl
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps \
	$RPM_BUILD_ROOT/etc/X11/applnk/Networking

make prefix=$RPM_BUILD_ROOT%{_prefix} install-strip

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Networking
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/%{name}
/etc/X11/applnk/Networking/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat May 13 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.9.4-4]
- modified spec file for PLD use,
- recompiled on rpm 3,
- package is FHS 2.0 compliant.

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.4

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.3

* Mon Mar 8 1999 Michael Fulbright <drmike@redhat.com>
- version 0.9.2

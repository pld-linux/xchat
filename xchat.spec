Summary:	Gtk+ IRC client
Summary(pl):	Oparty na Gtk+ klient IRC
Name:		xchat
Version:	1.0.0
Release:	1
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Copyright:	Freely distributable
URL:		http://xchat.org/
Source0:	http://xchat.org/files/%{name}-%{version}.tar.gz
Source1:	xchat.desktop
Source2:	xchat.png
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6

%description
X-Chat is yet another IRC client for the X Window System, using the Gtk+
toolkit. It is pretty easy to use compared to the other Gtk+ IRC clients and
the interface is quite nicely designed.

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System, wykorzystuj±cym
bibliotekê Gtk+. Jest ca³kiem prosty w u¿yciu, w porównaniu do innych,
opartych na Gtk+ klientów IRC, a jego interfejs jest dosyæ ³adnie
zaprojektowany.

%prep
%setup -q

%build
gettextize --copy --force
%configure \
	--disable-gnome \
	--disable-perl

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps \
	$RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking

make DESTDIR=$RPM_BUILD_ROOT install-strip

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf README ChangeLog AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS}.gz doc/*.html
%attr(755,root,root) %{_bindir}/%{name}
/usr/X11R6/share/applnk/Networking/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

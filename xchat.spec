Summary:	Gtk+ IRC client
Summary(de):	Gtk+ IRC-Client
Summary(fr):	Client IRC Gtk+
Summary(pl):	Oparty na Gtk+ klient IRC
Name:		xchat
Version:	1.5.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://xchat.org/files/source/1.5/%{name}-%{version}.tar.bz2
Icon:		xchat.xpm
URL:		http://xchat.org/
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	imlib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-core-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
X-Chat is yet another IRC client for the X Window System, using the
Gtk+ toolkit. It is pretty easy to use compared to the other Gtk+ IRC
clients and the interface is quite nicely designed.

%description -l de
X-Chat ist ein IRC-Client für X-Windows, der Gtk+ benutzt.

%description -l fr
X-Chat est encore un autre client IRC pour le Système X Window,
utilisant le toolkit Gtk+. Il est plutot facile à utiliser comparé aux
autres clients IRC Gtk+ et son interface est assez bien conçue.

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj±cym bibliotekê Gtk+. Jest ca³kiem prosty w u¿yciu, w
porównaniu do innych, opartych na Gtk+ klientów IRC, a jego interfejs
jest dosyæ ³adnie zaprojektowany.

%prep
%setup -q

%build
rm -f config.status
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-gnome \
	--disable-perl

(cd po; make update-po)

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Networking/IRC

gzip -9nf README ChangeLog AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS}.gz doc/*html
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Networking/IRC/xchat.desktop
%{_datadir}/pixmaps/xchat.png

Summary:	Gtk+ IRC client
Summary(de):	Gtk+ IRC-Client
Summary(fr):	Client IRC Gtk+
Summary(pl):	Oparty na Gtk+ klient IRC
Name:		xchat
Version:	1.7.4
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://xchat.org/files/source/1.7/%{name}-%{version}.tar.bz2
Patch0:		%{name}-po.patch
Icon:		xchat.xpm
URL:		http://xchat.org/
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
BuildRequires:	python-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%patch0 -p1

%build
rm -f config.status missing
gettextize --copy --force
aclocal
autoconf
automake -a -c --foreign
%configure \
	--disable-perl \
	--enable-openssl \
	--enable-ipv6 \
	--enable-japanese-conv

%{__make} -C po update-po
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Network/IRC

install xchat.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/IRC
install xchat.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/

gzip -9nf README ChangeLog AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS}.gz doc/*html
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/IRC/xchat.desktop
%{_pixmapsdir}/xchat.png

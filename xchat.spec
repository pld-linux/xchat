Summary:	Gtk+ IRC client
Summary(de):	Gtk+ IRC-Client
Summary(es):	Cliente IRC Gnome
Summary(fr):	Client IRC Gtk+
Summary(pl):	Oparty na Gtk+ klient IRC
Summary(pt_BR):	Cliente IRC Gnome
Summary(ru):	Gtk+ IRC ������
Summary(uk):	Gtk+ IRC �̦���
Name:		xchat
Version:	1.8.9
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/1.8/%{name}-%{version}.tar.bz2
Source1:	%{name}-pl.po
Patch0:		%{name}-ac.patch
Patch1:		%{name}-fix-USE_GNOME.patch
Patch2:		%{name}-fix-default-replace.patch
Icon:		xchat.xpm
URL:		http://xchat.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	perl-devel
BuildRequires:	python-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X-Chat is yet another IRC client for the X Window System, using the
Gtk+ toolkit. It is pretty easy to use compared to the other Gtk+ IRC
clients and the interface is quite nicely designed.

%description -l de
X-Chat ist ein IRC-Client f�r X-Windows, der Gtk+ benutzt.

%description -l es
Cliente IRC Gnome.

%description -l fr
X-Chat est encore un autre client IRC pour le Syst�me X Window,
utilisant le toolkit Gtk+. Il est plutot facile � utiliser compar� aux
autres clients IRC Gtk+ et son interface est assez bien con�ue.

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj�cym bibliotek� Gtk+. Jest ca�kiem prosty w u�yciu, w
por�wnaniu do innych, opartych na Gtk+ klient�w IRC, a jego interfejs
jest dosy� �adnie zaprojektowany.

%description -l pt_BR
Cliente IRC Gnome.

%description -l ru
X-Chat - ��� ���� IRC ������ ��� X Window System, ������������
�������������� Gtk+. �� �������� ����� � ������������� � ��������� �
������� Gtk+ IRC-��������� � ����� �������� ������� �������������
���������.

%description -l uk
X-Chat - �� ���� IRC �̦��� ��� X Window System, ���� ����������դ
�����������Ҧ� Gtk+. ��� ������ ������ � ����������Φ ��Ҧ����� �
������ Gtk+ IRC-�̦������ �� ��� ������ ��ɤ��� ����������� ���������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} po/pl.po

%build
rm -f config.status missing
%{__gettextize}
aclocal
%{__autoconf}
automake -a -c --foreign
%configure \
	--enable-perl \
	--enable-openssl \
	--enable-japanese-conv \
	--enable-ipv6

%{__make} -C po update-po
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	utildir=%{_applnkdir}/Network/Communications

install xchat.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install xchat.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS doc/*html
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/xchat.desktop
%{_pixmapsdir}/xchat.png

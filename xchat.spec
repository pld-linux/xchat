Summary:	A GTK+ IRC (chat) client
Summary(cs):	Gtk+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	Gtk+ IRC-Client
Summary(es):	Cliente Gtk+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client Gtk+ IRC (chat)
Summary(ja):	GTK+ IRC (����å�) ���饤�����
Summary(ko):	GTK+ IRC (ä��) Ŭ���̾�Ʈ
Summary(no):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na Gtk+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC Gnome
Summary(ru):	Gtk+ IRC ������ (chat)
Summary(sk):	IRC klient zalo�en� na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	Gtk+ IRC �̦���
Summary(zh_CN):	GTK+ IRC (����) �ͻ���
Name:		xchat
Version:	1.8.9
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/1.8/%{name}-%{version}.tar.bz2
Source1:	%{name}-pl.po
Patch0:		http://xchat.org/files/source/1.8/patches/xc189fixnoti.diff
Patch10:	%{name}-ac.patch
Patch11:	%{name}-fix-USE_GNOME.patch
Patch12:	%{name}-fix-default-replace.patch
Patch13:	%{name}-UTF8_desktop.patch
Patch14:	%{name}-zh.patch
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

%description -l cs
Chat je IRC klient pro X Window System napsan� v Gtk+. Je snadno
ovladateln� a na rozd�l od jin�ch Gtk+ IRC klient� je jeho rozhran�
velmi p�kn� navr�en�.

%description -l da
X-Chat er en IRC-klient for X11 og GTK+.  X-Chat er ganske enkelt at
bruge og har en p�n gr�nseflade.

%description -l de
X-Chat ist ein weiterer IRC-Client f�r das X Window System und GTK+.
X-Chat ist sehr leicht zu bedienen, und das Interface ist ganz attraktiv
gestaltet.

%description -l es
X-chat es otro cliente de IRC para X Window, que utiliza el toolkit
Gtk+. Es sencillo de usar frente a otros clientes de hechos con Gtk+
y la interfaz esta bien dise�ada.

%description -l fr
X-Chat est encore un autre client IRC pour le Syst�me X Window,
utilisant le toolkit Gtk+. Il est plutot facile � utiliser compar� aux
autres clients IRC Gtk+ et son interface est assez bien con�ue.

%description -l id
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is
X-Chat er enn eitt IRC forriti� fyrir X gluggakerfi� og GTK+.
X-Chat er frekar einfaldur � notkun mi�a� vi� �nnur GTK+ IRC
forrit, og h�nnun notendavi�m�tsins er frekar smart.

%description -l it
X-Chat � un client IRC per X Window, che usa il Toolkit Gtk+.
� semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja
X-Chat �� X Window System ����� GTK+ �Τ⤦�ҤȤĤ� IRC
���饤����ȤǤ���X-Chat �ϡ�¾�� GTK+ IRC ���饤����Ȥ���٤�
�Ȥ��䤹����ͥ�줿���󥿡��ե������߷פˤʤäƤ��ޤ���

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj�cym bibliotek� Gtk+. Jest ca�kiem prosty w u�yciu, w
por�wnaniu do innych, opartych na Gtk+ klient�w IRC, a jego interfejs
jest dosy� �adnie zaprojektowany.

%description -l pt
O X-Chat � mais outro cliente IRC para o X Window System e GTK+.
O X-Chat � relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - ��� ���� IRC ������ ��� X Window System, ������������
�������������� Gtk+. �� �������� ����� � ������������� � ��������� �
������� Gtk+ IRC-��������� � ����� �������� ������� �������������
���������.

%description -l sk
X-Chat je �al�� z IRC klientov pre syst�m X Window
pou��vaj�ci kni�nicu Gtk+. V porovnan� s in�mi na Gtk+
zalo�en�mi IRC klientami je pomerne �ahko pou�ite�n�
a m� celkom pekne navrhnut� rozhranie.
Nain�talujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat �r en IRC-klient f�r X11 och GTK+. X-Chat �r ganska enkelt att
anv�nda och har ett trevligt gr�nssnitt.

%description -l uk
X-Chat - �� ���� IRC �̦��� ��� X Window System, ���� ����������դ
�����������Ҧ� Gtk+. ��� ������ ������ � ����������Φ ��Ҧ����� �
������ Gtk+ IRC-�̦������ �� ��� ������ ��ɤ��� ����������� ���������.

%prep
%setup -q
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

cp %{SOURCE1} po/pl.po
rm -f po/zh_TW.Big5.gmo
mv -f po/zh_TW.Big5.po po/zh_TW.po

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

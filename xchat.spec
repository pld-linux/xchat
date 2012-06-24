Summary:	A GTK+ IRC (chat) client
Summary(cs):	GTK+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	GTK+ IRC-Client
Summary(es):	Cliente GTK+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client GTK+ IRC (chat)
Summary(ja):	GTK+ IRC (����å�) ���饤�����
Summary(ko):	GTK+ IRC (ä��) Ŭ���̾�Ʈ
Summary(nb):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na GTK+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC GNOME
Summary(ru):	GTK+ IRC ������ (chat)
Summary(sk):	IRC klient zalo�en� na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	GTK+ IRC �̦���
Summary(zh_CN):	GTK+ IRC (����) �ͻ���
Name:		xchat
Version:	2.4.0
Release:	3
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	084585b765509d5da355155189b16ecd
Source1:	%{name}-pl.po
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
Patch2:		%{name}-long-delimiter.patch
Patch3:		%{name}-domains.patch
Icon:		xchat.xpm
URL:		http://xchat.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Chat is yet another IRC client for the X Window System, using the
GTK+ toolkit. It is pretty easy to use compared to the other GTK+ IRC
clients and the interface is quite nicely designed.

%description -l cs
Chat je IRC klient pro X Window System napsan� v GTK+. Je snadno
ovladateln� a na rozd�l od jin�ch GTK+ IRC klient� je jeho rozhran�
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
GTK+. Es sencillo de usar frente a otros clientes de hechos con GTK+
y la interfaz esta bien dise�ada.

%description -l fr
X-Chat est encore un autre client IRC pour le Syst�me X Window,
utilisant le toolkit GTK+. Il est plutot facile � utiliser compar� aux
autres clients IRC GTK+ et son interface est assez bien con�ue.

%description -l id
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is
X-Chat er enn eitt IRC forriti� fyrir X gluggakerfi� og GTK+.
X-Chat er frekar einfaldur � notkun mi�a� vi� �nnur GTK+ IRC
forrit, og h�nnun notendavi�m�tsins er frekar smart.

%description -l it
X-Chat � un client IRC per X Window, che usa il Toolkit GTK+.
� semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja
X-Chat �� X Window System ����� GTK+ �Τ⤦�ҤȤĤ� IRC
���饤����ȤǤ���X-Chat �ϡ�¾�� GTK+ IRC ���饤����Ȥ���٤�
�Ȥ��䤹����ͥ�줿���󥿡��ե������߷פˤʤäƤ��ޤ���

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj�cym bibliotek� GTK+. Jest ca�kiem prosty w u�yciu, w
por�wnaniu do innych, opartych na GTK+ klient�w IRC, a jego interfejs
jest dosy� �adnie zaprojektowany.

%description -l pt
O X-Chat � mais outro cliente IRC para o X Window System e GTK+.
O X-Chat � relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - ��� ���� IRC ������ ��� X Window System, ������������
�������������� GTK+. �� �������� ����� � ������������� � ��������� �
������� GTK+ IRC-��������� � ����� �������� ������� �������������
���������.

%description -l sk
X-Chat je �al�� z IRC klientov pre syst�m X Window
pou��vaj�ci kni�nicu GTK+. V porovnan� s in�mi na GTK+
zalo�en�mi IRC klientami je pomerne �ahko pou�ite�n�
a m� celkom pekne navrhnut� rozhranie.
Nain�talujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat �r en IRC-klient f�r X11 och GTK+. X-Chat �r ganska enkelt att
anv�nda och har ett trevligt gr�nssnitt.

%description -l uk
X-Chat - �� ���� IRC �̦��� ��� X Window System, ���� ����������դ
�����������Ҧ� GTK+. ��� ������ ������ � ����������Φ ��Ҧ����� �
������ GTK+ IRC-�̦������ �� ��� ������ ��ɤ��� ����������� ���������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{no,nb}.po
cp %{SOURCE1} po/pl.po

%build
rm -f config.status missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-gnome \
	--enable-panel \
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
	utildir=%{_desktopdir}

mv -f %{name}.desktop %{name}.desktop.orig
sed -e 's/Network;/Network;InstantMessaging;/' %{name}.desktop.orig > %{name}.desktop

install xchat.desktop $RPM_BUILD_ROOT%{_desktopdir}
install xchat.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog faq.html HACKING README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xchat
%dir %{_libdir}/xchat/plugins
%attr(755,root,root) %{_libdir}/xchat/plugins/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

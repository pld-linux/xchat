Summary:	A GTK+ IRC (chat) client
Summary(cs):	Gtk+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	Gtk+ IRC-Client
Summary(es):	Cliente Gtk+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client Gtk+ IRC (chat)
Summary(ja):	GTK+ IRC (¥Á¥ã¥Ã¥È) ¥¯¥é¥¤¥¢¥ó¥È
Summary(ko):	GTK+ IRC (Ã¤ÆÃ) Å¬¶óÀÌ¾ğÆ®
Summary(no):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na Gtk+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC Gnome
Summary(ru):	Gtk+ IRC ËÌÉÅÎÔ (chat)
Summary(sk):	IRC klient zalo¾enı na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	Gtk+ IRC ËÌ¦¤ÎÔ
Summary(zh_CN):	GTK+ IRC (ÁÄÌì) ¿Í»§¡£
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
Chat je IRC klient pro X Window System napsanı v Gtk+. Je snadno
ovladatelnı a na rozdíl od jinıch Gtk+ IRC klientù je jeho rozhraní
velmi pìknì navr¾ené.

%description -l da
X-Chat er en IRC-klient for X11 og GTK+.  X-Chat er ganske enkelt at
bruge og har en pæn grænseflade.

%description -l de
X-Chat ist ein weiterer IRC-Client für das X Window System und GTK+.
X-Chat ist sehr leicht zu bedienen, und das Interface ist ganz attraktiv
gestaltet.

%description -l es
X-chat es otro cliente de IRC para X Window, que utiliza el toolkit
Gtk+. Es sencillo de usar frente a otros clientes de hechos con Gtk+
y la interfaz esta bien diseñada.

%description -l fr
X-Chat est encore un autre client IRC pour le Système X Window,
utilisant le toolkit Gtk+. Il est plutot facile à utiliser comparé aux
autres clients IRC Gtk+ et son interface est assez bien conçue.

%description -l id
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is
X-Chat er enn eitt IRC forritiğ fyrir X gluggakerfiğ og GTK+.
X-Chat er frekar einfaldur í notkun miğağ viğ önnur GTK+ IRC
forrit, og hönnun notendaviğmótsins er frekar smart.

%description -l it
X-Chat è un client IRC per X Window, che usa il Toolkit Gtk+.
È semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja
X-Chat ¤Ï X Window System ¤ª¤è¤Ó GTK+ ¤Î¤â¤¦¤Ò¤È¤Ä¤Î IRC
¥¯¥é¥¤¥¢¥ó¥È¤Ç¤¹¡£X-Chat ¤Ï¡¢Â¾¤Î GTK+ IRC ¥¯¥é¥¤¥¢¥ó¥È¤ÈÈæ¤Ù¤Æ
»È¤¤¤ä¤¹¤¯¡¢Í¥¤ì¤¿¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹Àß·×¤Ë¤Ê¤Ã¤Æ¤¤¤Ş¤¹¡£

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj±cym bibliotekê Gtk+. Jest ca³kiem prosty w u¿yciu, w
porównaniu do innych, opartych na Gtk+ klientów IRC, a jego interfejs
jest dosyæ ³adnie zaprojektowany.

%description -l pt
O X-Chat é mais outro cliente IRC para o X Window System e GTK+.
O X-Chat é relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - ÅİÅ ÏÄÉÎ IRC ËÌÉÅÎÔ ÄÌÑ X Window System, ÉÓĞÏÌØÚÕÀİÉÊ
ÉÎÓÔÒÕÍÅÎÔÁÒÉÊ Gtk+. ïÎ ÄÏ×ÏÌØÎÏ ÌÅÇÏË × ÉÓĞÏÌØÚÏ×ÁÎÉÉ × ÓÒÁ×ÎÅÎÉÉ Ó
ÄÒÕÇÉÍÉ Gtk+ IRC-ËÌÉÅÎÔÁÍÉ É ÉÍÅÅÔ ÄÏ×ÏÌØÎÏ ĞÒÉÑÔÎÏ ÒÁÚÒÁÂÏÔÁÎÎÙÊ
ÉÎÔÅÒÆÅÊÓ.

%description -l sk
X-Chat je ïal¹í z IRC klientov pre systém X Window
pou¾ívajúci kni¾nicu Gtk+. V porovnaní s inımi na Gtk+
zalo¾enımi IRC klientami je pomerne µahko pou¾iteµnı
a má celkom pekne navrhnuté rozhranie.
Nain¹talujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat är en IRC-klient för X11 och GTK+. X-Chat är ganska enkelt att
använda och har ett trevligt gränssnitt.

%description -l uk
X-Chat - İÅ ÏÄÉÎ IRC ËÌ¦¤ÎÔ ÄÌÑ X Window System, ÑËÉÊ ×ÉËÏÒÉÓÔÏ×Õ¤
¦ÎÓÔÒÕÍÅÎÔÁÒ¦Ê Gtk+. ÷¦Î ÄÏÓÉÔØ ÌÅÇËÉÊ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ĞÏÒ¦×ÎÑÎÏ Ú
¦ÎÛÉÍÉ Gtk+ IRC-ËÌ¦¤ÎÔÁÍÉ ÔÁ ÍÁ¤ ÄÏÓÉÔØ ĞÒÉ¤ÍÎÏ ÒÏÚÒÏÂÌÅÎÉÊ ¦ÎÔÅÒÆÅÊÓ.

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

Summary:	A GTK+ IRC (chat) client
Summary(cs):	GTK+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	GTK+ IRC-Client
Summary(es):	Cliente GTK+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client GTK+ IRC (chat)
Summary(ja):	GTK+ IRC (¥Á¥ã¥Ã¥È) ¥¯¥é¥¤¥¢¥ó¥È
Summary(ko):	GTK+ IRC (Ã¤ÆÃ) Å¬¶óÀÌ¾ðÆ®
Summary(nb):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na GTK+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC GNOME
Summary(ru):	GTK+ IRC ËÌÉÅÎÔ (chat)
Summary(sk):	IRC klient zalo¾ený na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	GTK+ IRC ËÌ¦¤ÎÔ
Summary(zh_CN):	GTK+ IRC (ÁÄÌì) ¿Í»§¡£
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
Chat je IRC klient pro X Window System napsaný v GTK+. Je snadno
ovladatelný a na rozdíl od jiných GTK+ IRC klientù je jeho rozhraní
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
GTK+. Es sencillo de usar frente a otros clientes de hechos con GTK+
y la interfaz esta bien diseñada.

%description -l fr
X-Chat est encore un autre client IRC pour le Système X Window,
utilisant le toolkit GTK+. Il est plutot facile à utiliser comparé aux
autres clients IRC GTK+ et son interface est assez bien conçue.

%description -l id
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is
X-Chat er enn eitt IRC forritið fyrir X gluggakerfið og GTK+.
X-Chat er frekar einfaldur í notkun miðað við önnur GTK+ IRC
forrit, og hönnun notendaviðmótsins er frekar smart.

%description -l it
X-Chat è un client IRC per X Window, che usa il Toolkit GTK+.
È semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja
X-Chat ¤Ï X Window System ¤ª¤è¤Ó GTK+ ¤Î¤â¤¦¤Ò¤È¤Ä¤Î IRC
¥¯¥é¥¤¥¢¥ó¥È¤Ç¤¹¡£X-Chat ¤Ï¡¢Â¾¤Î GTK+ IRC ¥¯¥é¥¤¥¢¥ó¥È¤ÈÈæ¤Ù¤Æ
»È¤¤¤ä¤¹¤¯¡¢Í¥¤ì¤¿¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹Àß·×¤Ë¤Ê¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj±cym bibliotekê GTK+. Jest ca³kiem prosty w u¿yciu, w
porównaniu do innych, opartych na GTK+ klientów IRC, a jego interfejs
jest dosyæ ³adnie zaprojektowany.

%description -l pt
O X-Chat é mais outro cliente IRC para o X Window System e GTK+.
O X-Chat é relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - ÅÝÅ ÏÄÉÎ IRC ËÌÉÅÎÔ ÄÌÑ X Window System, ÉÓÐÏÌØÚÕÀÝÉÊ
ÉÎÓÔÒÕÍÅÎÔÁÒÉÊ GTK+. ïÎ ÄÏ×ÏÌØÎÏ ÌÅÇÏË × ÉÓÐÏÌØÚÏ×ÁÎÉÉ × ÓÒÁ×ÎÅÎÉÉ Ó
ÄÒÕÇÉÍÉ GTK+ IRC-ËÌÉÅÎÔÁÍÉ É ÉÍÅÅÔ ÄÏ×ÏÌØÎÏ ÐÒÉÑÔÎÏ ÒÁÚÒÁÂÏÔÁÎÎÙÊ
ÉÎÔÅÒÆÅÊÓ.

%description -l sk
X-Chat je ïal¹í z IRC klientov pre systém X Window
pou¾ívajúci kni¾nicu GTK+. V porovnaní s inými na GTK+
zalo¾enými IRC klientami je pomerne µahko pou¾iteµný
a má celkom pekne navrhnuté rozhranie.
Nain¹talujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat är en IRC-klient för X11 och GTK+. X-Chat är ganska enkelt att
använda och har ett trevligt gränssnitt.

%description -l uk
X-Chat - ÝÅ ÏÄÉÎ IRC ËÌ¦¤ÎÔ ÄÌÑ X Window System, ÑËÉÊ ×ÉËÏÒÉÓÔÏ×Õ¤
¦ÎÓÔÒÕÍÅÎÔÁÒ¦Ê GTK+. ÷¦Î ÄÏÓÉÔØ ÌÅÇËÉÊ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ÐÏÒ¦×ÎÑÎÏ Ú
¦ÎÛÉÍÉ GTK+ IRC-ËÌ¦¤ÎÔÁÍÉ ÔÁ ÍÁ¤ ÄÏÓÉÔØ ÐÒÉ¤ÍÎÏ ÒÏÚÒÏÂÌÅÎÉÊ ¦ÎÔÅÒÆÅÊÓ.

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

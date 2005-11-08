Summary:	A GTK+ IRC (chat) client
Summary(cs):	GTK+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	GTK+ IRC-Client
Summary(es):	Cliente GTK+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client GTK+ IRC (chat)
Summary(ja):	GTK+ IRC (ΑγΓΘ) ��ιⅳⅱτΘ
Summary(ko):	GTK+ IRC (채팅) 클라이언트
Summary(nb):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na GTK+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC GNOME
Summary(ru):	GTK+ IRC 盖�턱� (chat)
Summary(sk):	IRC klient zalo푘n� na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	GTK+ IRC 盖┐塊
Summary(zh_CN):	GTK+ IRC (좔莖) 와빵。
Name:		xchat
Version:	2.6.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	0c827bf6df0572231cbbb1e25965fb61
Source1:	%{name}-pl.po
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
Patch2:		%{name}-long-delimiter.patch
Patch3:		%{name}-domains.patch
Icon:		xchat.xpm
URL:		http://www.xchat.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
Requires:	GConf2
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Chat is yet another IRC client for the X Window System, using the
GTK+ toolkit. It is pretty easy to use compared to the other GTK+ IRC
clients and the interface is quite nicely designed.

%description -l cs
Chat je IRC klient pro X Window System napsan� v GTK+. Je snadno
ovladateln� a na rozd�l od jin�ch GTK+ IRC klient� je jeho rozhran�
velmi p�kn� navr푘n�.

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
X-Chat ㅟ X Window System ㄺㅸㅣ GTK+ ㅞㅲㄶㅢㅘㅔㅞ IRC
��ιⅳⅱτΘㅗㅉ。X-Chat ㅟ、쩐ㅞ GTK+ IRC ��ιⅳⅱτΘㅘ흑ㅩㅖ
뽁ㄴㅴㅉㄿ、磎ㅼㅏⅳτ�에샵樂㎘ㄵ뮌芟壘胛價채튄ㄴ蜚묀�

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj켧ym bibliotek� GTK+. Jest ca쿸iem prosty w u퓓ciu, w
por�wnaniu do innych, opartych na GTK+ klient�w IRC, a jego interfejs
jest dosy� 쿪dnie zaprojektowany.

%description -l pt
O X-Chat � mais outro cliente IRC para o X Window System e GTK+.
O X-Chat � relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - 텟� 謳�� IRC 盖�턱� 켈� X Window System, �唐驅媒藍憤�
�傀同郞턱讀虜� GTK+. 停 켓凜景卦 謙하� � �唐驅媒窘죔�� � 塘죽壙炚� �
켠朗�苽 GTK+ IRC-盖�턱讀苽 � �考텃 켓凜景卦 妗�喇卦 怒撲좌鞫죔槐�
�塊텀팍柬.

%description -l sk
X-Chat je �al뱁 z IRC klientov pre syst�m X Window
pou얩vaj�ci kni푣icu GTK+. V porovnan� s in�mi na GTK+
zalo푘n�mi IRC klientami je pomerne 킳hko pou푝te탇�
a m� celkom pekne navrhnut� rozhranie.
Nain퉡alujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat �r en IRC-klient f�r X11 och GTK+. X-Chat �r ganska enkelt att
anv�nda och har ett trevligt gr�nssnitt.

%description -l uk
X-Chat - 墳 謳�� IRC 盖┐塊 켈� X Window System, 麒�� 慄蓋虜戇窘邏
┧戇論考塊죠┟ GTK+. 憚� 켓譚潼 謙핌�� � 慄蓋虜戇죔過 饉娘肋吉� �
┧排苽 GTK+ IRC-盖┐塊죌� 讀 皐� 켓譚潼 妗�ㅝ卦 碌撲苟謙炚� ┧旽盧탱�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%{_sysconfdir}/gconf/schemas/apps_xchat_url_handler.schemas

Summary:	A GTK+ IRC (chat) client
Summary(cs):	Gtk+ IRC (chat) klient
Summary(da):	En GTK+ IRC (Tjat) klient
Summary(de):	Gtk+ IRC-Client
Summary(es):	Cliente Gtk+ IRC (chat)
Summary(fr):	Client IRC GTK+ (discussion)
Summary(id):	Program GTK+ untuk chatting
Summary(is):	IRC spjallforrit sem notar GTK+
Summary(it):	Client Gtk+ IRC (chat)
Summary(ja):	GTK+ IRC (ΑγΓΘ) ��ιⅳⅱτΘ
Summary(ko):	GTK+ IRC (채팅) 클라이언트
Summary(no):	En GTK+-basert IRC-klient
Summary(pl):	Oparty na Gtk+ klient IRC
Summary(pt):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR):	Cliente IRC Gnome
Summary(ru):	Gtk+ IRC 盖�턱� (chat)
Summary(sk):	IRC klient zalo푘n� na GTK+
Summary(sl):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv):	En GTK+-IRC- (chatt-)klient
Summary(uk):	Gtk+ IRC 盖┐塊
Summary(zh_CN):	GTK+ IRC (좔莖) 와빵。
Name:		xchat
Version:	2.0.2
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/2.0/%{name}-%{version}.tar.bz2
#Source1:	%{name}-pl.po
#Patch0:		%{name}-po.patch
Icon:		xchat.xpm
URL:		http://xchat.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:  glib2-devel >= 2.0.3
BuildRequires:	openssl-devel >= 0.9.7
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
X-Chat ㅟ X Window System ㄺㅸㅣ GTK+ ㅞㅲㄶㅢㅘㅔㅞ IRC
��ιⅳⅱτΘㅗㅉ。X-Chat ㅟ、쩐ㅞ GTK+ IRC ��ιⅳⅱτΘㅘ흑ㅩㅖ
뽁ㄴㅴㅉㄿ、磎ㅼㅏⅳτ�에샵樂㎘ㄵ뮌芟壘胛價채튄ㄴ蜚묀�

%description -l pl
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystuj켧ym bibliotek� Gtk+. Jest ca쿸iem prosty w u퓓ciu, w
por�wnaniu do innych, opartych na Gtk+ klient�w IRC, a jego interfejs
jest dosy� 쿪dnie zaprojektowany.

%description -l pt
O X-Chat � mais outro cliente IRC para o X Window System e GTK+.
O X-Chat � relativamente simples de usar e tem uma interface gira.

%description -l ru
X-Chat - 텟� 謳�� IRC 盖�턱� 켈� X Window System, �唐驅媒藍憤�
�傀同郞턱讀虜� Gtk+. 停 켓凜景卦 謙하� � �唐驅媒窘죔�� � 塘죽壙炚� �
켠朗�苽 Gtk+ IRC-盖�턱讀苽 � �考텃 켓凜景卦 妗�喇卦 怒撲좌鞫죔槐�
�塊텀팍柬.

%description -l sk
X-Chat je �al뱁 z IRC klientov pre syst�m X Window
pou얩vaj�ci kni푣icu Gtk+. V porovnan� s in�mi na Gtk+
zalo푘n�mi IRC klientami je pomerne 킳hko pou푝te탇�
a m� celkom pekne navrhnut� rozhranie.
Nain퉡alujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv
X-Chat �r en IRC-klient f�r X11 och GTK+. X-Chat �r ganska enkelt att
anv�nda och har ett trevligt gr�nssnitt.

%description -l uk
X-Chat - 墳 謳�� IRC 盖┐塊 켈� X Window System, 麒�� 慄蓋虜戇窘邏
┧戇論考塊죠┟ Gtk+. 憚� 켓譚潼 謙핌�� � 慄蓋虜戇죔過 饉娘肋吉� �
┧排苽 Gtk+ IRC-盖┐塊죌� 讀 皐� 켓譚潼 妗�ㅝ卦 碌撲苟謙炚� ┧旽盧탱�.

%prep
%setup -q
#%patch0 -p1

#cp %{SOURCE1} po/pl.po

%build
rm -f config.status missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
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
	utildir=%{_applnkdir}/Network/Communications

install xchat.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install xchat.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS 
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xchat
%dir %{_libdir}/xchat/plugins
%attr(755,root,root) %{_libdir}/xchat/plugins/*
%{_applnkdir}/Network/Communications/xchat.desktop
%{_pixmapsdir}/xchat.png

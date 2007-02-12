Summary:	A GTK+ IRC (chat) client
Summary(cs.UTF-8):   Gtk+ IRC (chat) klient
Summary(da.UTF-8):   En GTK+ IRC (Tjat) klient
Summary(de.UTF-8):   Gtk+ IRC-Client
Summary(es.UTF-8):   Cliente Gtk+ IRC (chat)
Summary(fr.UTF-8):   Client IRC GTK+ (discussion)
Summary(id.UTF-8):   Program GTK+ untuk chatting
Summary(is.UTF-8):   IRC spjallforrit sem notar GTK+
Summary(it.UTF-8):   Client Gtk+ IRC (chat)
Summary(ja.UTF-8):   GTK+ IRC (チャット) クライアント
Summary(ko.UTF-8):   GTK+ IRC (채팅) 클라이언트
Summary(nb.UTF-8):   En GTK+-basert IRC-klient
Summary(pl.UTF-8):   Oparty na Gtk+ klient IRC
Summary(pt.UTF-8):   Um cliente de IRC (chat) em GTK+
Summary(pt_BR.UTF-8):   Cliente IRC GNOME
Summary(ru.UTF-8):   Gtk+ IRC клиент (chat)
Summary(sk.UTF-8):   IRC klient založený na GTK+
Summary(sl.UTF-8):   Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv.UTF-8):   En GTK+-IRC- (chatt-)klient
Summary(uk.UTF-8):   Gtk+ IRC клієнт
Summary(zh_CN.UTF-8):   GTK+ IRC (聊天) 客户。
Name:		xchat
Version:	2.1.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	3af79df1c1b95a7ee143fcbe938b7bda
Source1:	%{name}-pl.po
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Chat is yet another IRC client for the X Window System, using the
Gtk+ toolkit. It is pretty easy to use compared to the other Gtk+ IRC
clients and the interface is quite nicely designed.

%description -l cs.UTF-8
Chat je IRC klient pro X Window System napsaný v Gtk+. Je snadno
ovladatelný a na rozdíl od jiných Gtk+ IRC klientů je jeho rozhraní
velmi pěkně navržené.

%description -l da.UTF-8
X-Chat er en IRC-klient for X11 og GTK+.  X-Chat er ganske enkelt at
bruge og har en pæn grænseflade.

%description -l de.UTF-8
X-Chat ist ein weiterer IRC-Client für das X Window System und GTK+.
X-Chat ist sehr leicht zu bedienen, und das Interface ist ganz attraktiv
gestaltet.

%description -l es.UTF-8
X-chat es otro cliente de IRC para X Window, que utiliza el toolkit
Gtk+. Es sencillo de usar frente a otros clientes de hechos con Gtk+
y la interfaz esta bien diseñada.

%description -l fr.UTF-8
X-Chat est encore un autre client IRC pour le Système X Window,
utilisant le toolkit Gtk+. Il est plutot facile à utiliser comparé aux
autres clients IRC Gtk+ et son interface est assez bien conçue.

%description -l id.UTF-8
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is.UTF-8
X-Chat er enn eitt IRC forritið fyrir X gluggakerfið og GTK+.
X-Chat er frekar einfaldur í notkun miðað við önnur GTK+ IRC
forrit, og hönnun notendaviðmótsins er frekar smart.

%description -l it.UTF-8
X-Chat è un client IRC per X Window, che usa il Toolkit Gtk+.
È semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja.UTF-8
X-Chat は X Window System および GTK+ のもうひとつの IRC
クライアントです。X-Chat は、他の GTK+ IRC クライアントと比べて
使いやすく、優れたインターフェイス設計になっています。

%description -l pl.UTF-8
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystującym bibliotekę Gtk+. Jest całkiem prosty w użyciu, w
porównaniu do innych, opartych na Gtk+ klientów IRC, a jego interfejs
jest dosyć ładnie zaprojektowany.

%description -l pt.UTF-8
O X-Chat é mais outro cliente IRC para o X Window System e GTK+.
O X-Chat é relativamente simples de usar e tem uma interface gira.

%description -l ru.UTF-8
X-Chat - еще один IRC клиент для X Window System, использующий
инструментарий Gtk+. Он довольно легок в использовании в сравнении с
другими Gtk+ IRC-клиентами и имеет довольно приятно разработанный
интерфейс.

%description -l sk.UTF-8
X-Chat je ďalší z IRC klientov pre systém X Window
používajúci knižnicu Gtk+. V porovnaní s inými na Gtk+
založenými IRC klientami je pomerne ľahko použiteľný
a má celkom pekne navrhnuté rozhranie.
Nainštalujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv.UTF-8
X-Chat är en IRC-klient för X11 och GTK+. X-Chat är ganska enkelt att
använda och har ett trevligt gränssnitt.

%description -l uk.UTF-8
X-Chat - ще один IRC клієнт для X Window System, який використовує
інструментарій Gtk+. Він досить легкий у використанні порівняно з
іншими Gtk+ IRC-клієнтами та має досить приємно розроблений інтерфейс.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

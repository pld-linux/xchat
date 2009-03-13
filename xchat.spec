Summary:	A GTK+ IRC (chat) client
Summary(cs.UTF-8):	GTK+ IRC (chat) klient
Summary(da.UTF-8):	En GTK+ IRC (Tjat) klient
Summary(de.UTF-8):	GTK+ IRC-Client
Summary(es.UTF-8):	Cliente GTK+ IRC (chat)
Summary(fr.UTF-8):	Client IRC GTK+ (discussion)
Summary(id.UTF-8):	Program GTK+ untuk chatting
Summary(is.UTF-8):	IRC spjallforrit sem notar GTK+
Summary(it.UTF-8):	Client GTK+ IRC (chat)
Summary(ja.UTF-8):	GTK+ IRC (チャット) クライアント
Summary(ko.UTF-8):	GTK+ IRC (채팅) 클라이언트
Summary(nb.UTF-8):	En GTK+-basert IRC-klient
Summary(pl.UTF-8):	Oparty na GTK+ klient IRC
Summary(pt.UTF-8):	Um cliente de IRC (chat) em GTK+
Summary(pt_BR.UTF-8):	Cliente IRC GNOME
Summary(ru.UTF-8):	GTK+ IRC клиент (chat)
Summary(sk.UTF-8):	IRC klient založený na GTK+
Summary(sl.UTF-8):	Odjemnik v GTK+ za IRC (internetni klepet)
Summary(sv.UTF-8):	En GTK+-IRC- (chatt-)klient
Summary(uk.UTF-8):	GTK+ IRC клієнт
Summary(zh_CN.UTF-8):	GTK+ IRC (聊天) 客户。
Name:		xchat
Version:	2.8.6
Release:	4
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://xchat.org/files/source/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	1f2670865d43a23a9abc596dde999aca
Source1:	%{name}-pl.po
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locale_names.patch
Patch2:		%{name}-long-delimiter.patch
Patch3:		%{name}-domains.patch
Patch4:		%{name}-smallfixes.patch
Patch5:		%{name}-gtk_2_14.patch
URL:		http://www.xchat.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.10
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	libsexy-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,preun):	GConf2
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Chat is yet another IRC client for the X Window System, using the
GTK+ toolkit. It is pretty easy to use compared to the other GTK+ IRC
clients and the interface is quite nicely designed.

%description -l cs.UTF-8
Chat je IRC klient pro X Window System napsaný v GTK+. Je snadno
ovladatelný a na rozdíl od jiných GTK+ IRC klientů je jeho rozhraní
velmi pěkně navržené.

%description -l da.UTF-8
X-Chat er en IRC-klient for X11 og GTK+. X-Chat er ganske enkelt at
bruge og har en pæn grænseflade.

%description -l de.UTF-8
X-Chat ist ein weiterer IRC-Client für das X Window System und GTK+.
X-Chat ist sehr leicht zu bedienen, und das Interface ist ganz attraktiv
gestaltet.

%description -l es.UTF-8
X-chat es otro cliente de IRC para X Window, que utiliza el toolkit
GTK+. Es sencillo de usar frente a otros clientes de hechos con GTK+
y la interfaz esta bien diseñada.

%description -l fr.UTF-8
X-Chat est encore un autre client IRC pour le Système X Window,
utilisant le toolkit GTK+. Il est plutot facile à utiliser comparé aux
autres clients IRC GTK+ et son interface est assez bien conçue.

%description -l id.UTF-8
X-Chat adalah IRC client lain untuk X Window System dan GTK+.
X-Chat sangat mudah digunakan, dibandingkan dengan GTK+ IRC client
lainnya, dan interfacenya didesain dengan bagus.

%description -l is.UTF-8
X-Chat er enn eitt IRC forritið fyrir X gluggakerfið og GTK+.
X-Chat er frekar einfaldur í notkun miðað við önnur GTK+ IRC
forrit, og hönnun notendaviðmótsins er frekar smart.

%description -l it.UTF-8
X-Chat è un client IRC per X Window, che usa il Toolkit GTK+.
È semplice da usare e comprende un'interfaccia molto gradevole.

%description -l ja.UTF-8
X-Chat は X Window System および GTK+ のもうひとつの IRC
クライアントです。X-Chat は、他の GTK+ IRC クライアントと比べて
使いやすく、優れたインターフェイス設計になっています。

%description -l pl.UTF-8
X-Chat jest jeszcze jednym klientem IRC dla X Window System,
wykorzystującym bibliotekę GTK+. Jest całkiem prosty w użyciu, w
porównaniu do innych, opartych na GTK+ klientów IRC, a jego interfejs
jest dosyć ładnie zaprojektowany.

%description -l pt.UTF-8
O X-Chat é mais outro cliente IRC para o X Window System e GTK+.
O X-Chat é relativamente simples de usar e tem uma interface gira.

%description -l ru.UTF-8
X-Chat - еще один IRC клиент для X Window System, использующий
инструментарий GTK+. Он довольно легок в использовании в сравнении с
другими GTK+ IRC-клиентами и имеет довольно приятно разработанный
интерфейс.

%description -l sk.UTF-8
X-Chat je ďalší z IRC klientov pre systém X Window
používajúci knižnicu GTK+. V porovnaní s inými na GTK+
založenými IRC klientami je pomerne ľahko použiteľný
a má celkom pekne navrhnuté rozhranie.
Nainštalujte xchat, ak potrebujete IRC klienta pre X.

%description -l sv.UTF-8
X-Chat är en IRC-klient för X11 och GTK+. X-Chat är ganska enkelt att
använda och har ett trevligt gränssnitt.

%description -l uk.UTF-8
X-Chat - ще один IRC клієнт для X Window System, який використовує
інструментарій GTK+. Він досить легкий у використанні порівняно з
іншими GTK+ IRC-клієнтами та має досить приємно розроблений інтерфейс.

%prep
%setup -q
%patch0 -p1
# xchat-pl.po needs update
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
	--enable-ipv6 \
	--enable-japanese-conv \
	--enable-openssl \
	--enable-panel \
	--enable-perl \
	--enable-shm

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

%post
%gconf_schema_install apps_xchat_url_handler.schemas

%preun
%gconf_schema_uninstall apps_xchat_url_handler.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog faq.html HACKING README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xchat
%dir %{_libdir}/xchat/plugins
%attr(755,root,root) %{_libdir}/xchat/plugins/*
%{_datadir}/dbus-1/services/org.xchat.service.service
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_sysconfdir}/gconf/schemas/apps_xchat_url_handler.schemas

#
# TODO: - place locales in /usr/share/locale
#	- pass our FLAGS
#
Summary:	Futuristic real-time strategy game
Summary(pl.UTF-8):	Futurystyczna gra strategiczna czasu rzeczywistego
Name:		boswars
Version:	2.6.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.boswars.org/dist/releases/%{name}-%{version}-src.tar.gz
# Source0-md5:	7f0fcf440e8d765c484f09074f993b40
URL:		http://www.boswars.org/
BuildRequires:	SDL-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	lua51-devel
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bos Wars is a futuristic real-time strategy game (RTS). It is possible
to play against human opponents over LAN, internet, or against the
computer.

%description -l pl.UTF-8
Bos Wars to futurystyczna gra strategiczna czasu rzeczywistego (RTS).
Posiada możliwość gry przez sieć przeciwko innym graczom lub przeciwko
graczom sterowanym przez komputer.

%prep
%setup -q -n %{name}-%{version}-src

%build
%{scons}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

install boswars $RPM_BUILD_ROOT%{_bindir}/boswars.run
find -maxdepth 1 -mindepth 1 -type d -exec sh -c 'cp -r "{}" $RPM_BUILD_ROOT%{_datadir}/%{name}' \;

# create start script
cat > $RPM_BUILD_ROOT%{_bindir}/boswars << EOF
#!/bin/sh

%{_bindir}/boswars.run -d %{_datadir}/%{name}
EOF

rm -rf  $RPM_BUILD_ROOT%{_datadir}/%{name}/{doc,build,.sconf_temp}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.txt
%attr(755,root,root) %{_bindir}/boswars
%attr(755,root,root) %{_bindir}/boswars.run
%{_datadir}/%{name}

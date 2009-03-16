Summary:	Curses-based 3270 Emulator
Name:		c3270
Version: 3.3.6
Release: 	%mkrel 4
License:	GPL
Group:		Terminals
URL:		http://www.geocities.com/SiliconValley/Peaks/7814/
Source0:	c3270-%{version}.tgz
Patch:	c3270-3.3-fix-format-errors.patch
Requires:	x3270 <= %{version}
Requires:	readline
BuildRequires:	X11-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	libtermcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep
%setup -q -n %{name}-3.3
%patch -p 1

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

%build

%configure2_5x \
    --without-pr3287 

%make %{name}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 %{name} %{buildroot}%{_bindir}/
install -m644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/Bugs.html html/Build.html html/FAQ.html html/Intro.html
%doc html/Lineage.html html/New.html html/README.html 
%doc html/Wishlist.html html/c3270-man.html README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

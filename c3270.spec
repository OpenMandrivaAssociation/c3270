Summary:	Curses-based 3270 Emulator
Name:		c3270
Version:	3.3.9ga12
Release: 	%mkrel 1
License:	GPL
Group:		Terminals
URL:		http://www.geocities.com/SiliconValley/Peaks/7814/
Source0:	http://downloads.sourceforge.net/project/x3270/x3270/%version/suite3270-%version.tgz
Patch:		c3270-3.3-fix-format-errors.patch
Requires:	x3270 <= %{version}
Requires:	readline
BuildRequires:	ncursesw-devel
BuildRequires:	readline-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep
%setup -q -n %{name}-3.3

%build
%configure2_5x \
    --without-pr3287 

%make %{name}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/*.html README
%{_sysconfdir}/x3270/ibm_hosts
%{_bindir}/*

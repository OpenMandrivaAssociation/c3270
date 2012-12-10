Summary:	Curses-based 3270 Emulator
Name:		c3270
Version:	3.3.9ga12
Release: 	%mkrel 4
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

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%_bindir/x3270if

install -d %{buildroot}%{_mandir}/man1
install -m644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/*.html README
%{_sysconfdir}/x3270/ibm_hosts
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.9ga12-4mdv2011.0
+ Revision: 610091
- rebuild

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 3.3.9ga12-3mdv2010.1
+ Revision: 533667
- rebuild for openssl 1.0

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 3.3.9ga12-2mdv2010.0
+ Revision: 415334
- fix file list

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 3.3.9ga12-1mdv2010.0
+ Revision: 415324
- New version 3.3.9ga12

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.6-4mdv2009.1
+ Revision: 356293
- fix format errors

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.3.6-3mdv2009.0
+ Revision: 243396
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3.6-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Jun 27 2007 Funda Wang <fwang@mandriva.org> 3.3.6-1mdv2008.0
+ Revision: 44857
- New version
- Import c3270



* Tue Aug 01 2006 Lenny Cartier <lenny@mandriva.com> 3.3.2p2-4mdv2007.0
- rebuild

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.3.2p2-3mdk
- rebuilt against openssl-0.9.8a

* Fri Feb  4 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 3.3.2p2-2mdk
- rebuilt against new readline

* Thu Jul 22 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 3.3.2p2-1mdk
- new version

* Tue Jun 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 3.3.2p1-1mdk
- new version
- fix strange perms
- fix deps

* Fri Jul 11 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.20-1mdk
- 3.2.20
- use the %%configure2_5x macro

* Mon Jan 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-3mdk
- build release
- misc spec file fixes

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.2.19-2mdk
- rebuild for new readline

* Thu May 16 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-1mdk
- new version
- misc spec file fixes
- rebuilt with latest system compiler (gcc3.1)

* Tue Jan  1 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.18-1mdk
- new version

* Mon Sep 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.2.17-1mdk
- added in contribs by Oden Eriksson <oden.eriksson@kvikkjokk.net> :
	- initial cooker contrib

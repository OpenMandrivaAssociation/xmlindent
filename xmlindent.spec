%define	name	xmlindent
%define	version	0.2.17
%define release	8

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Summary:	XML stream reformatter
Group:		Development/Other
License:	GPL
URL:		http://xmlindent.sf.net/
Source0:	http://dl.sf.net/xmlindent/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	flex

%description
XML Indent is a XML stream reformatter written in ANSI C.
It is analogous to GNU indent.

%prep
%setup -q
sed -i -e "s,-Wall,-Wall \$(CFLAGS),g" -e "s,555,755," -e "s,444,644," Makefile

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog BUGS README LICENSE
%{_bindir}/xmlindent
%{_mandir}/man1/xmlindent.1*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.2.17-7mdv2010.0
+ Revision: 435150
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.2.17-6mdv2009.0
+ Revision: 140966
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.2.17-6mdv2008.1
+ Revision: 130306
- kill re-definition of %%buildroot on Pixel's request
- import xmlindent


* Wed Oct 05 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.17-6mdk
- mandriva release based on fedora

* Wed Jun 08 2005 Adrian Reber <adrian@lisas.de> - 0.2.17-5
- rebuilt

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.2.17-4
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Dec 07 2004 Adrian Reber <adrian@lisas.de> - 0:0.2.17-2
- applied patch from Ville Skyttä (bug #2078)

* Fri Sep 17 2004 Adrian Reber <adrian@lisas.de> - 0:0.2.17-0.fdr.1
- Initial RPM release.

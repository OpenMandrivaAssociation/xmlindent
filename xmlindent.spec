%define	name	xmlindent
%define	version	0.2.17
%define	release	7

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


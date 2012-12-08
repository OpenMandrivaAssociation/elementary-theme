%define tarname	elementary-theme
%define name	elementary-theme
%define version	2.4
%define release %mkrel 8

Summary:	Elementary theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
#Theme for openbox
Source1:	%{tarname}-openbox.tar.gz
#fix scrollbar issues
#Patch0:		elementary-ooo-lo.patch
#fix color for complete view with kde4 rosa theme
#Patch1:		mdk_rosa_theme.patch
Patch2:		elementary-theme-2.4.scrollbar-color.patch
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	murrine
Requires:	gtk-aurora-engine
Suggests:	elementary-icons

%description
Elementary theme.

%prep
%setup -q -a1
#% patch0 -p0
#% patch1 -p0

# elementary-theme-2.4.scrollbar-color.patch
%patch2 -p1 -b .color

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/themes
%__mkdir -p %{buildroot}%{_datadir}/themes/elementary
cp -rf elementary/* %{buildroot}%{_datadir}/themes/elementary

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/themes/*



%changelog
* Fri Aug 12 2011 Alexander Barakin <abarakin@mandriva.org> 2.4-7mdv2011.0
+ Revision: 694235
- scrollbar_color is no longer supported #63823

  + Alex Burmashev <burmashev@mandriva.org>
    - updated elementary theme

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 2.4-5
+ Revision: 684685
- add openbox theme

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 2.4-4
+ Revision: 684398
- simplicify for ROSA KDE4 theme

* Mon Jun 13 2011 Александр Казанцев <kazancas@mandriva.org> 2.4-3
+ Revision: 684383
- openoffice.org and libreoffice scrollbar disappear fix

* Sun May 01 2011 Funda Wang <fwang@mandriva.org> 2.4-2
+ Revision: 661120
- add missign requires on extra packages

* Mon Apr 11 2011 Alex Burmashev <burmashev@mandriva.org> 2.4-1
+ Revision: 652631
- import elementary-theme


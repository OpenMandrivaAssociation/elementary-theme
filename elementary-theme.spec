%define tarname	elementary-theme
%define name	elementary-theme
%define version	2.4
%define release %mkrel 6

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
Patch1:		mdk_rosa_theme.patch
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	murrine
Requires:	gtk-aurora-engine
Suggests:	elementary-icons

%description
Elementary theme.

%prep
%setup -q -a1
#%patch0 -p0
%patch1 -p0

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


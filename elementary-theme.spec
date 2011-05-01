%define tarname	elementary-theme
%define name	elementary-theme
%define version	2.4
%define release %mkrel 2

Summary:	Elementary theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
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
%setup -q

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


Summary:	Elementary theme
Name:		elementary-theme
Version:	2.4
Release:	15
License:	GPLv2
Group:		Graphical desktop/Other
Source0:	%{name}-%{version}.tar.gz
#Theme for openbox
Source1:	%{name}-openbox.tar.gz
#fix scrollbar issues
#Patch0:		elementary-ooo-lo.patch
#fix color for complete view with kde4 rosa theme
#Patch1:		mdk_rosa_theme.patch
Patch2:		elementary-theme-2.4.scrollbar-color.patch
BuildArch:	noarch

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes
mkdir -p %{buildroot}%{_datadir}/themes/elementary
cp -rf elementary/* %{buildroot}%{_datadir}/themes/elementary

%files
%{_datadir}/themes/*


Name:           myrlyn
Version:        0.9.9
Release:        1
Summary:        Myrlyn package manager GUI for Linux 
License:        GPL-2.0-only
Group:          System/Packages
URL:            https://github.com/shundhammer/myrlyn
Source0:        https://github.com/shundhammer/myrlyn/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libzypp) >= 17.21.0
BuildRequires:  imagemagick
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.17
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core) >= 6.5
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Svg)
Requires: %{_lib}Qt6Svg
Requires:	xdg-utils
Requires: zypper

%description
Myrlyn is a graphical package manager to select software packages
and patterns for installation, update and removal.

It uses libzypp as its backend and Qt as its GUI toolkit.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/myrlyn
%{_bindir}/myrlyn-askpass
%{_bindir}/myrlyn-sudo
%{_datadir}/applications/%{name}-*.desktop
%{_datadir}/icons/hicolor/*/apps/Myrlyn.png

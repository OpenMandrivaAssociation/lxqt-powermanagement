%define git 0
Name: lxqt-powermanagement
Version: 0.13.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: Power management module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb-screensaver)
BuildRequires: pkgconfig(xcb-dpms)
BuildRequires: lxqt-build-tools git-core

%description
Power management module for LXQt.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches

%cmake_qt5 -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%find_lang %{name} --with-qt
%find_lang lxqt-config-powermanagement --with-qt

%files -f %{name}.lang -f lxqt-config-powermanagement.lang
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/laptop-lid.svg
%{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_*.qm
%{_sysconfdir}/xdg/autostart/lxqt-powermanagement.desktop

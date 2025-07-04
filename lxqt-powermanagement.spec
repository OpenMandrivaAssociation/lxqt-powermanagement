#define git 0
Name: lxqt-powermanagement
Version: 2.2.1
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-powermanagement/releases/download/%{version}/lxqt-powermanagement-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}1
Summary: Power management module for LXQt
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Source1: lxqt-powermanagement.conf
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-globalkeys-ui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6SvgWidgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(qt6xdg)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb-screensaver)
BuildRequires: pkgconfig(xcb-dpms)
BuildRequires: lxqt-build-tools git-core

%description
Power management module for LXQt.

%prep
%autosetup -p1 -n %{name}-%{?git:%{git}}%{!?git:%{version}}

%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-G Ninja

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
mkdir -p %{buildroot}%{_datadir}/lxqt
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/lxqt/lxqt-powermanagement.conf

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/lxqt/lxqt-powermanagement.conf
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/laptop-lid.svg
%{_sysconfdir}/xdg/autostart/lxqt-powermanagement.desktop
%dir %{_datadir}/lxqt/translations/lxqt-config-powermanagement
%dir %{_datadir}/lxqt/translations/lxqt-powermanagement

%define git 0
Name: lxqt-powermanagement
Version: 1.0.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 2
Source0: https://github.com/lxqt/lxqt-powermanagement/releases/download/%{version}/lxqt-powermanagement-%{version}.tar.xz
%endif
Summary: Power management module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Source1: lxqt-powermanagement.conf
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-globalkeys-ui)
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
%autopatch -p1

%cmake_qt5 \
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
%lang(arn) %{_datadir}/lxqt/translations/lxqt-config-powermanagement/lxqt-config-powermanagement_arn.qm
%lang(ast) %{_datadir}/lxqt/translations/lxqt-config-powermanagement/lxqt-config-powermanagement_ast.qm
%lang(arn) %{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_arn.qm
%lang(ast) %{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_ast.qm

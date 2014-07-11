Name: lxqt-powermanagement
Version: 0.7.0
Release: 3
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Patch0: lxqt-powermanagement-0.7.0-compile.patch
Summary: Power management module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel

%description
Power management module for LXQt

%prep
%setup -q -c %{name}-%{version}
%apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/laptop-lid.svg

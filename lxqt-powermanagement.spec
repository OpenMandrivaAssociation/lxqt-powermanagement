%define git 0
Name: lxqt-powermanagement
Version: 0.9.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 2
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: Power management module for LXQt
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt5-devel
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: desktop-file-utils

%description
Power management module for LXQt

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-config-powermanagement.desktop

%find_lang %{name} --with-qt
%find_lang lxqt-config-powermanagement --with-qt

%files -f %{name}.lang -f lxqt-config-powermanagement.lang
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*/laptop-lid.svg
%{_datadir}/lxqt/translations/lxqt-powermanagement/lxqt-powermanagement_*.qm

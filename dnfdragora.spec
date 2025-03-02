# Force out of source build
%undefine __cmake_in_source_build

Name:		dnfdragora
Version:	3.0.0
Release:	2%{?dist}
Summary:	DNF package-manager based on libYui abstraction

License:	GPL-3.0-or-later
URL:		https://github.com/huakim/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	cmake			>= 3.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig
BuildRequires:	python3-devel		>= 3.4.0
BuildRequires:	python3-libdnf5		>= 5.2.7
BuildRequires:	python3-manatools	>= 0.0.3
BuildRequires:	python3-PyYAML
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
BuildRequires:	python3-yui
BuildRequires:	python3-pyxdg
BuildRequires:	python3-cairosvg
BuildRequires:	python3-pillow
BuildRequires:	python3-pystray		>= 0.16

Requires:	dnf5daemon-server	>= 5.2.7
Requires:	filesystem
Requires:	comps-extras
Requires:	hicolor-icon-theme
Requires:	libyui-mga-ncurses
Requires:	python3-libdnf5		>= 5.2.7
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-PyYAML
Requires:	python3-yui		>= 1.1.1-10

Provides:	%{name}-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-qt if qt6-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)

%description
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.


%package updater
Summary:	Update notifier applet for %{name}

Requires:	%{name}			== %{version}-%{release}
Requires:	libnotify
Requires:	python3-pyxdg
Requires:	python3-cairosvg
Requires:	python3-pillow
Requires:	python3-pystray		>= 0.16

Obsoletes:	%{name}-gui		< 1.0.1-7

%description updater
%{name} is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

%{name} is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.

This package provides the update notifier applet for %{name}.


%prep
%autosetup -p 1


%build
%cmake \
  -DCHECK_RUNTIME_DEPENDENCIES=ON \
  -DENABLE_COMPS=ON               \
  %{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name}


%check
# Validate desktop-files.
desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/*.desktop

# Validate AppData-files.
appstream-util validate-relax --nonet		\
	%{buildroot}%{_datadir}/appdata/*.appdata.xml


%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yaml
%dir %{_sysconfdir}/%{name}
%doc README.md %{name}.yaml*.example
%exclude %{python3_sitelib}/%{name}/updater.py
%exclude %{python3_sitelib}/%{name}/__pycache__/updater.cpython*.py?
%license AUTHORS LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/applications/*%{name}-localinstall.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man5/%{name}*.5*
%{_mandir}/man8/%{name}*.8*
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*


%files updater
%{_bindir}/%{name}-updater
%{_datadir}/applications/*%{name}-updater.desktop
%{_sysconfdir}/xdg/autostart/*%{name}*.desktop
%{python3_sitelib}/%{name}/updater.py
%{python3_sitelib}/%{name}/__pycache__/updater.cpython*.py?



%changelog
* Wed Mar 2 2025 huakim tylyktar <fijik19@gmail.com> - 3.0.0-2
- Version 3.0.0

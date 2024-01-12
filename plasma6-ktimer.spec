%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-ktimer
Summary:	Execute programs after some time
Version:	24.01.90
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/ktimer
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ktimer-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)

%description
KTimer is a little tool to execute programs after some time.

%files -f ktimer.lang
%{_bindir}/ktimer
%{_iconsdir}/*/*/apps/ktimer.*
%{_datadir}/applications/org.kde.ktimer.desktop
%{_datadir}/metainfo/org.kde.ktimer.appdata.xml

#######################################################################


%prep
%autosetup -p1 -n ktimer-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ktimer --with-html

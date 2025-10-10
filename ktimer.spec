#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ktimer
Summary:	Execute programs after some time
Version:	25.08.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		https://utils.kde.org/projects/ktimer
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/ktimer/-/archive/%{gitbranch}/ktimer-%{gitbranchd}.tar.bz2#/ktimer-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ktimer-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(Qt6Core5Compat)

%rename plasma6-ktimer

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KTimer is a little tool to execute programs after some time.

%files -f %{name}.lang
%{_bindir}/ktimer
%{_iconsdir}/*/*/apps/ktimer.*
%{_datadir}/applications/org.kde.ktimer.desktop
%{_datadir}/metainfo/org.kde.ktimer.appdata.xml

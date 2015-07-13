Name:		ktimer
Summary:	Execute programs after some time
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/ktimer
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)

%description
KTimer is a little tool to execute programs after some time.

%files
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_usr}/shareapplications/org.kde.%{name}.desktop
%doc %{_docdir}/HTML/*/%{name}


#######################################################################


%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build



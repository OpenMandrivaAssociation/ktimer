Name:		ktimer
Summary:	Execute programs after some time
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/ktimer
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)


%description
KTimer is a little tool to execute programs after some time.

%files
%{_bindir}/ktimer
%{_iconsdir}/*/*/apps/ktimer.*
%{_datadir}applications/org.kde.ktimer.desktop
%doc %{_docdir}/HTML/*/ktimer


#######################################################################


%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build



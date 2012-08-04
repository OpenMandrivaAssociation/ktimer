Name:		ktimer
Summary:	Execute programs after some time
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/ktimer
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KTimer is a little tool to execute programs after some time.

%files
%{_kde_bindir}/ktimer
%{_kde_iconsdir}/*/*/apps/ktimer.*
%{_kde_applicationsdir}/ktimer.desktop
%{_kde_docdir}/HTML/*/ktimer

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


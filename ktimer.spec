Name: ktimer
Summary: Execute programs after some time
Version: 4.7.95
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL: http://utils.kde.org/projects/ktimer
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

Obsoletes: %name-ktimer < 3.93.0-0.714053.1
Obsoletes: kde4-ktimer < 4.0.68
Provides: kde4-ktimer = %version
 	
%description
KTimer is a little tool to execute programs after some time.

%files 
%defattr(-,root,root)
%_kde_bindir/ktimer
%_kde_iconsdir/*/*/apps/ktimer.*
%_kde_datadir/applications/kde4/ktimer.desktop
%_kde_docdir/HTML/*/ktimer

%prep
%setup -q

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build


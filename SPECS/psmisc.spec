%global package_speccommit 833f3771cc7827630c52e1ac8422a1e24a653208
%global usver 23.6
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}

Summary: Utilities for managing processes on your system
Name: psmisc
Version: 23.6
Release: %{?xsrel}%{?dist}
License: GPLv2+
URL: https://gitlab.com/psmisc/psmisc

Source0: psmisc-23.6.tar.xz

BuildRequires: make
BuildRequires: gettext
BuildRequires: ncurses-devel
BuildRequires: autoconf automake
BuildRequires: gcc
BuildRequires: git


%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall, fuser and pslog.  The pstree command displays
a tree structure of all of the running processes on your system.  The
killall command sends a specified signal (SIGTERM if nothing is specified)
to processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems. The pslog
command shows the path of log files owned by a given process.

%prep
%autosetup -S git

%build
%configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
make install DESTDIR="$RPM_BUILD_ROOT"

mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT%{_sbindir}

%find_lang %name --all-name --with-man


%files -f %{name}.lang
%{_sbindir}/fuser
%{_bindir}/killall
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_bindir}/prtstat
%{_bindir}/pslog
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pslog.1*
%ifarch %{ix86} x86_64 ppc %{power64} %{arm} aarch64 mipsel
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1*
%else
%exclude %{_mandir}/man1/peekfd.1*
%endif
%license COPYING
%doc AUTHORS ChangeLog README


%changelog
* Fri Dec 20 2024 Stephen Cheng <stephen.cheng@cloud.com> - 23.6-2
- CA-403405: Build for xs8

* Thu Aug 24 2023 Lin Liu <lin.liu@citrix.com> - 23.6-1
- First imported release


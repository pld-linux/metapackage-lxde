Summary:	LX Desktop Environment with additional packages
Name:		metapackage-lxde
Version:	0.1
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	gpicview
Requires:	lxappearance
Requires:	lxde-common
Requires:	lxde-icon-theme
Requires:	lxinput
Requires:	lxmenu-data
Requires:	lxnm
Requires:	lxpanel
Requires:	lxrandr
Requires:	lxsession
Requires:	lxsession-edit
Requires:	lxshortcut
Requires:	lxtask
Requires:	lxterminal
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "Lightweight X11 Desktop Environment" is an extremely
fast-performing and energy-saving desktop environment.

Maintained by an international community of developers, it comes with
a beautiful interface, multi-language support, standard keyboard short
cuts and additional features like tabbed file browsing.

LXDE uses less CPU and less RAM than other environments. It is
especially designed for cloud computers with low hardware
specifications, such as, netbooks, mobile devices (e.g. MIDs) or older
computers.

%description -l pl.UTF-8
Środowisko graficzne KDE4 z dodatkowymi pakietami (metapakiet).

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
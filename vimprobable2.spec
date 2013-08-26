Summary:	Lean web browser optimised for full keyboard control
Name:		vimprobable2
Version:	1.3.0
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sourceforge/vimprobable/Releases/%{name}_%{version}.tar.bz2
# Source0-md5:	474edf9bf1eb55e1ec7c0adaba7b93f5
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
BuildRequires:	gtk+-webkit-devel
BuildRequires:	libsoup-devel
BuildRequires:	perl
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
Requires(post,postun):	desktop-file-utils
Requires:	glib-networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vimprobable is a web browser that behaves like the Vimperator plugin
available for Mozilla Firefox. It is based on the WebKit engine (using
GTK+ bindings). The goal of Vimprobable is to build a completely
keyboard-driven, efficient and pleasurable browsing-experience.
Its featureset might be considered "minimalistic", but not as
minimalistic as being completely featureless.

%prep
%setup -qn %{name}
%patch0 -p1

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc LICENSE PATCHES
%attr(755,root,root) %{_bindir}/vimprobable2
%{_desktopdir}/vimprobable2.desktop
%{_pixmapsdir}/vimprobable2.png
%{_mandir}/man1/vimprobable2.1*
%{_mandir}/man5/vimprobablerc.5*


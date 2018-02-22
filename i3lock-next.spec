Name:           i3lock-next
Version:        f29ac60bb5856412ff0ff5c2b7887c7ce432f0b7
Release:        1%{?dist}
Summary:        i3lock-next is a Python 3 script and C helper program much like i3lock-fancy.

License:        BSD
URL:            https://github.com/torvitas/i3lock-next.spec
Source0:        https://github.com/owenthewizard/i3lock-next/archive/f29ac60bb5856412ff0ff5c2b7887c7ce432f0b7.tar.gz

BuildRequires:  imlib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libXrandr-devel
Requires:       i3lock-color
Requires:       imlib2
Requires:       bash
Requires:       fontconfig
Requires:       libXrandr

%global debug_package %{nil}

%description
i3lock-next is a Python 3 script and C helper program much like i3lock-fancy. i3lock-next aims to be much faster by using Imlib2 rather than ImageMagick, and being written (mostly) in C.

%prep
%autosetup

%build
%make_build PREFIX=/usr/


%install
rm -rf %{buildroot}
%make_install PREFIX=/usr


%files
%license LICENSE
%doc README.md
%{_bindir}/i3lock-next
/usr/libexec/i3lock-next/i3lock-next-helper
/usr/share/i3lock-next/lock-dark.png
/usr/share/i3lock-next/lock-light.png

%changelog
* Thu Feb 22 2018 Sascha Marcel Schmidt <mail@saschaschmidt.net>
- Initial version of the package.

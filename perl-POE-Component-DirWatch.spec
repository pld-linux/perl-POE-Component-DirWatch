#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-DirWatch
Summary:	POE::Component::DirWatch - POE directory watcher
Summary(pl.UTF-8):   POE::Component::DirWatch - obserwowanie katalogów w POE
Name:		perl-POE-Component-DirWatch
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d41814d4a100c10f270c09638f193ccc
URL:		http://poe.perl.org/
BuildRequires:	perl-POE
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::DirWatch watches a directory for files. It creates a
separate session which invokes a user-supplied callback as soon as if
finds a file in the directory. Its primary intended use is processing
a "drop-box" style directory, such as an FTP upload directory.

%description -l pl.UTF-8
POE::Component::DirWatch obserwowuje katalog pod kątem plików. Tworzy
oddzielną sesję, która wywołuje przekazane przez użytkownika wywołanie
zwrotne zaraz jak znajdzie w katalogu plik. Głównym zastosowaniem jest
przetwarzanie katalogów służących do wrzucania plików, takich jak
katalog upload dostępny przez FTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/DirWatch.pm
%{_mandir}/man3/*

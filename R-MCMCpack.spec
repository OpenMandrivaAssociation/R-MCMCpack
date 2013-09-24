%global packname  MCMCpack
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.3
Release:          1
Summary:          Markov chain Monte Carlo (MCMC) Package
Group:            Sciences/Mathematics
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/MCMCpack_1.3-3.tar.gz
Requires:         R-coda R-MASS R-stats
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-coda R-MASS R-stats

%description
This package contains functions to perform Bayesian inference using
posterior simulation for a number of statistical models. Most simulation
is done in compiled C++ written in the Scythe Statistical Library Version
1.0.2. All models return coda mcmc objects that can then be summarized
using the coda package.  MCMCpack also contains some useful utility
functions, including some additional density functions and pseudo-random
number generators for statistical distributions, a general purpose
Metropolis sampling algorithm, and tools for visualization.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


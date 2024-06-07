use pyo3::prelude::*;
mod blacklist;
mod filter;
use filter::is_blacklisted;


#[pymodule]
fn holded_dataflow(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_blacklisted, m)?)?;
    Ok(())
}

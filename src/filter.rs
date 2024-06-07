use pyo3::prelude::pyfunction;
use pyo3::{exceptions::PyException, PyErr};

pub use crate::blacklist::{PIPELINE_BLACKLIST, SSGTM_BLACKLIST};

#[pyfunction]
pub fn is_blacklisted(name: &str, filter_type: &str) -> Result<bool, PyErr> {
    match filter_type {
        "PIPELINE" => {
            // Access the PIPELINE_BLACKLIST hashmap from blacklist.rs
            Ok(PIPELINE_BLACKLIST.contains_key(name))
        }
        "SSGTM" => {
            // Access the SSGTM_BLACKLIST hashmap from blacklist.rs
            Ok(SSGTM_BLACKLIST.contains_key(name))
        }
        _ => Err(PyErr::new::<PyException, _>("This FilterType is not implemented")),
    }
}

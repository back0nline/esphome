import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID

DEPENDENCIES = ['logger']

debug_ns = cg.esphome_ns.namespace('debug')
DebugComponent = debug_ns.class_('DebugComponent', cg.Component)
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_variable_id(DebugComponent),
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    rhs = DebugComponent.new()
    var = cg.Pvariable(config[CONF_ID], rhs)
    yield cg.register_component(var, config)
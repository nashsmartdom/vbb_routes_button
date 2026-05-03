from __future__ import annotations

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import VBBRoutesButtonCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities) -> None:
    coordinator: VBBRoutesButtonCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([VBBRefreshButton(coordinator, entry)])


class VBBRefreshButton(CoordinatorEntity[VBBRoutesButtonCoordinator], ButtonEntity):
    _attr_icon = "mdi:refresh"

    def __init__(self, coordinator: VBBRoutesButtonCoordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator)
        self.entry = entry
        self._attr_name = f"{entry.title} Refresh"
        self._attr_unique_id = f"{entry.entry_id}_refresh"
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, entry.entry_id)}, name=entry.title, manufacturer="VBB", model="Manual route query")

    async def async_press(self) -> None:
        await self.coordinator.async_request_refresh()

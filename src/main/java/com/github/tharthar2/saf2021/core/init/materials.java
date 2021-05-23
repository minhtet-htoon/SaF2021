package com.github.tharthar2.saf2021.core.init;

import com.github.tharthar2.saf2021.SaF2021;
import com.github.tharthar2.saf2021.integrations.FDS;
import com.github.tharthar2.saf2021.integrations.IDS;
import com.github.tharthar2.saf2021.integrations.LDS;
import com.oblivioussp.spartanweaponry.api.WeaponMaterial;
import com.oblivioussp.spartanweaponry.api.trait.WeaponTrait;
import net.minecraft.util.ResourceLocation;

public class materials {
    public static WeaponMaterial materialFDS = new WeaponMaterial("fire_dragonsteel", SaF2021.modid, 0x0F6363, 0x107272, 4, 8000, 15f, 30f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_fire"), new FDS("Fiery",SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialIDS = new WeaponMaterial("ice_dragonsteel", SaF2021.modid, 0x0F6363, 0x107272, 4, 8000, 15f, 30f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_ice"), new IDS("Icy", SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialLDS = new WeaponMaterial("lightning_dragonsteel", SaF2021.modid, 0x0F6363, 0x107272, 4, 8000, 15f, 30f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_lightning"), new LDS("Shocking", SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialFDB = new WeaponMaterial("fire_dragonbone", SaF2021.modid, 0x0F6363, 0x107272, 4, 2000, 10f, 20f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_lightning"), new FDS("Fiery", SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialIDB = new WeaponMaterial("ice_dragonbone", SaF2021.modid, 0x0F6363, 0x107272, 4, 2000, 10f, 20f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_lightning"), new IDS("Icy", SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialLDB = new WeaponMaterial("lightning_dragonbone", SaF2021.modid, 0x0F6363, 0x107272, 4, 2000, 10f, 20f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_lightning"), new LDS("Shocking", SaF2021.modid, WeaponTrait.TraitQuality.POSITIVE));
    public static WeaponMaterial materialDB = new WeaponMaterial("dragonbone", SaF2021.modid, 0x0F6363, 0x107272, 4, 2000, 15f, 10f, 69,
            new ResourceLocation("forge:ingots/dragonsteel_lightning"));
}

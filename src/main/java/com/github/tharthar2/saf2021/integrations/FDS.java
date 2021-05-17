package com.github.tharthar2.saf2021.integrations;


import com.oblivioussp.spartanweaponry.api.WeaponMaterial;
import com.oblivioussp.spartanweaponry.api.trait.MeleeCallbackWeaponTrait;
import net.minecraft.entity.Entity;
import net.minecraft.entity.LivingEntity;
import net.minecraft.item.ItemStack;

public class FDS extends MeleeCallbackWeaponTrait {


    public FDS(String propType, String propModId, TraitQuality quality) {
        super(propType, propModId, quality);
    }
    @Override
    public void onHitEntity(WeaponMaterial material, ItemStack stack, LivingEntity target,
                            LivingEntity attacker, Entity projectile) {
        target.setFire(15);
        target.applyKnockback( 1F, attacker.getPosX() - target.getPosX(), attacker.getPosZ() - target.getPosZ());
    }
}
